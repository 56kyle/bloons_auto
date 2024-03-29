BTD6 Memory Values
==================

Important Classes (At least for retrieving info)
------------------
- Assets
  - Scripts
    - Simulation
      - Input
        - InputManager (Assets.Scripts.Simulation.Input.InputManager)
          - [CanPlaceTowerAt](./Assets.Scripts.Simulation.Input.InputManager.CanPlaceTowerAt.txt)
            - Parameters
              - pos: Assets.Scripts.Simulation.SMath.Vector2
              - towerModel: Assets.Scripts.Models.Towers.TowerModel
              - coopZonePlaceValid: System.Boolean&
              - forTowerId: System.Int32
            - Returns
              - System.Boolean
          - [QueryPlacementPosition](./Assets.Scripts.Simulation.Input.InputManager.QueryPlacementPosition.txt)
            - Parameters
              - pos: Assets.Scripts.Simulation.SMath.Vector2
              - towerModel: Assets.Scripts.Models.Towers.TowerModel
              - forTowerId: System.Int32
            - Returns
              - Assets.Scripts.Unity.Bridge.PlacementQuery
      - Towers
        - Tower (Assets.Scripts.Simulation.Towers.Tower)
          - [Highlight](./Assets.Scripts.Simulation.Towers.Tower.Hilight.txt)
            - Parameters
              - None
            - Returns
              - System.Void
          - [UnHighlight](./Assets.Scripts.Simulation.Towers.Tower.UnHilight.txt)
            - Parameters
              - None
            - Returns
              - System.Void
        - TowerManager (Assets.Scripts.Simulation.Towers.TowerManager)
          - [CreateAreaPlaceholderTower](./Assets.Scripts.Simulation.Towers.TowerManager.CreateAreaPlaceholderTower.txt)
            - Parameters
              - def: Assets.Scripts.Models.Towers.TowerModel
              - position: Assets.Scripts.Simulation.SMath.Vector3
              - areaPlacedOn: System.Int32
              - owner: System.Int32
            - Returns
              - Assets.Scripts.Simulation.Towers.Tower
          - [CreateTower](./Assets.Scripts.Simulation.Towers.TowerManager.CreateTower.txt)
            - Parameters
              - def: Assets.Scripts.Models.Towers.TowerModel
              - position: Assets.Scripts.Simulation.SMath.Vector3
              - inputIndex: System.Int32
              - areaPlacedOn: System.Int32
              - parentTowerId: System.Int32
              - loadingSaveData: Assets.Scripts.Models.Profile.TowerSaveDataModel
              - isInstaTower: System.Boolean
            - Returns
              - Assets.Scripts.Simulation.Towers.Tower
      - Track
        - Map (Assets.Scripts.Simulation.Track.Map)
          - [CanPlace](./Assets.Scripts.Simulation.Track.Map.CanPlace.txt)
            - Parameters
              - at: Assets.Scripts.Simulation.SMath.Vector2
              - tm: Assets.Scripts.Models.Towers.TowerModel
              - forExistingTower: Assets.Scripts.Simulation.Towers.Tower
              - canPlaceReturnData: Assets.Scripts.Simulation.Track.CanPlaceReturnData
              - checkTowerOverlaps: System.Boolean
            - Returns
              - System.Boolean
    - Unity
      - Bridge
        - UnityToSimulation (Assets.Scripts.Unity.Bridge.UnityToSimulation)
          - [QueryPlacementPosition](./Assets.Scripts.Unity.Bridge.UnityToSimulation.QueryPlacementPosition.txt)
            - Parameters
              - pos: UnityEngine.Vector2
              - tm: Assets.Scripts.Models.Towers.TowerModel
              - inputId: System.Int32
              - forTowerId: System.Int32
            - Returns
              - Assets.Scripts.Unity.Bridge.PlacementQuery
      - UI_New
        - InGame
          - InGame (Assets.Scripts.Unity.UI_New.InGame.InGame)
            - [GetUIFromWorld](./Assets.Scripts.Unity.UI_New.InGame.InGame.GetUIFromWorld)
              - Parameters
                - worldPos: UnityEngine.Vector2
                - clamp: System.Boolean
              - Returns
                - UnityEngine.Vector2
            - [GetUnityWorldFromCursor](./Assets.Scripts.Unity.UI_New.InGame.InGame.GetUnityWorldFromCursor.txt)
              - Parameters
                - None
              - Returns
                - UnityEngine.Vector3
            - [ScreenPosToCanvas](./Assets.Scripts.Unity.UI_New.InGame.InGame.ScreenPosToCanvas.txt)
              - Parameters
                - screenPos: UnityEngine.Vector2
              - Returns
                - UnityEngine.Vector2
            - [ScreenPosToUI](./Assets.Scripts.Unity.UI_New.InGame.InGame.ScreenPosToUI.txt)
              - Parameters
                - screenPos: UnityEngine.Vector2
              - Returns
                - UnityEngine.Vector2
          - InputManager (Assets.Scripts.Unity.UI_New.InGame.InputManager)
            - [GetCursorPosition](./Assets.Scripts.Unity.UI_New.InGame.InputManager.GetCursorPosition.txt)
              - Parameters
                - None
              - Returns
                - UnityEngine.Vector2
            - [Update](./Assets.Scripts.Unity.UI_New.InGame.InputManager.Update.txt)
              - Parameters
                - None
              - Returns
                - System.Void()


