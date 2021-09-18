
import pytest
from ..cheat_engine_txt_to_data import *

example_lines = [
    '			base class\n',
    '				24ad343e970 : CustomAnimationComponent\n',
    '					static fields\n',
    '					fields\n',
    '						18 : target (type: UnityEngine.GameObject)\n',
    '						20 : duration (type: System.Single)\n',
    '						28 : curve (type: UnityEngine.AnimationCurve)\n',
    '						30 : isPlaying (type: System.Boolean)\n',
    '						31 : loop (type: System.Boolean)\n',
    '						32 : disableOnEnd (type: System.Boolean)\n',
    '						33 : stopPlayingOnEnd (type: System.Boolean)\n',
    '						34 : resetOnEnable (type: System.Boolean)\n',
    '						35 : updateAnimOnReset (type: System.Boolean)\n',
    '						38 : speedMultiplier (type: System.Single)\n',
    '						3c : useUnscaledTime (type: System.Boolean)\n',
    '						40 : targetTransform (type: UnityEngine.Transform)\n',
    '						48 : elapsed (type: System.Single)\n',
    '					methods\n',
    '						24ad3c017c0 : .ctor ():System.Void\n',
    '						24ad3c01590 : Awake ():System.Void\n',
    '						24ad3c01630 : DisableIfInvalid ():System.Boolean\n',
    '						24ad3c01770 : OnEnable ():System.Void\n',
    '						24ad3c01720 : Reset ():System.Void\n',
    '						24ad3c01680 : Trigger ():System.Void\n',
    '						24ad3c015e0 : Update ():System.Void\n',
    '						24ad3c016d0 : UpdateAnimation (currentTime: System.Single):System.Void\n',
]

def test_get_stripped_lines():
    print(get_stripped_lines(example_lines))
    assert get_stripped_lines(example_lines) == ['base class', '24ad343e970 : CustomAnimationComponent', 'static fields', 'fields', '18 : target (type: UnityEngine.GameObject)', '20 : duration (type: System.Single)', '28 : curve (type: UnityEngine.AnimationCurve)', '30 : isPlaying (type: System.Boolean)', '31 : loop (type: System.Boolean)', '32 : disableOnEnd (type: System.Boolean)', '33 : stopPlayingOnEnd (type: System.Boolean)', '34 : resetOnEnable (type: System.Boolean)', '35 : updateAnimOnReset (type: System.Boolean)', '38 : speedMultiplier (type: System.Single)', '3c : useUnscaledTime (type: System.Boolean)', '40 : targetTransform (type: UnityEngine.Transform)', '48 : elapsed (type: System.Single)', 'methods', '24ad3c017c0 : .ctor ():System.Void', '24ad3c01590 : Awake ():System.Void', '24ad3c01630 : DisableIfInvalid ():System.Boolean', '24ad3c01770 : OnEnable ():System.Void', '24ad3c01720 : Reset ():System.Void', '24ad3c01680 : Trigger ():System.Void', '24ad3c015e0 : Update ():System.Void', '24ad3c016d0 : UpdateAnimation (currentTime: System.Single):System.Void']


