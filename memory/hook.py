
from abc import ABC
from .exceptions import MissingKwargError
from .script_info import ScriptInfo
from typing import Union, Callable, SupportsInt


class Hook(ScriptInfo, ABC):
    offset = 0x0
    on_enter: Union[Callable, str, None]
    on_leave: Union[Callable, str, None]

    def __init__(self,
                 address: Union[str, None] = None,
                 on_enter: Union[Callable, str, None] = None,
                 on_leave: Union[Callable, str, None] = None,
                 **kwargs):
        super().__init__(address=address, **kwargs)
        self.address = address
        self.on_enter = on_enter
        self.on_leave = on_leave

    def __str__(self) -> str:
        if not self.address:
            raise MissingKwargError('Missing kwarg \'address\'')
        return self.code(self.address)

    def code(self, address) -> str:
        on_enter_text = self.on_enter_container()
        on_leave_text = self.on_leave_container()
        return f'''
        Interceptor.attach(ptr("{address}"), {{
            {on_enter_text}
            {on_leave_text}
        }});
        ''' if on_enter_text or on_leave_text else ''

    def on_enter_container(self) -> str:
        on_enter_content = self.on_enter_content()
        return f'''onEnter: function(args) {{
            {on_enter_content}
        }},
        ''' if on_enter_content else ''

    def on_enter_content(self) -> str:
        if callable(self.on_enter):
            return self.on_enter(**self.kwargs)
        return self.on_enter

    def on_leave_container(self) -> str:
        on_leave_content = self.on_leave_content()
        return f'''onLeave: function(args) {{
            {on_leave_content}
         }},
         ''' if on_leave_content else ''

    def on_leave_content(self) -> str:
        if callable(self.on_leave):
            return self.on_leave(**self.kwargs)
        return self.on_leave


placement_zone_offset = 0x529760
create_tower_offset = 0x9907a0  # Assets.Scripts.Simulation.Towers.TowerManager.CreateTower
is_eq_after_ref_check_offset = 0x6DE110  # Assets.Scripts.Models.SimulationBehaviors.CreateTowerActionSimBehaviorModel.IsEqualAfterReferenceCheck
area_place_holder_tower_offset = 0x9905A0  # Assets.Scripts.Simulation.Towers.TowerManager.CreateAreaPlaceholderTower
update_display_position_offset = 0x98EF70  # Assets.Scripts.Simulation.Towers.Props.Prop.UpdateDisplayPosition
