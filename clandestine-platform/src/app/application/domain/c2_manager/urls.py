from __future__ import annotations



C2_BASE_URL: str = f"/api/c2"
C2_INSTANCE_LIST: str = f"{C2_BASE_URL}/instances"
C2_LISTENERS: str = f"{C2_BASE_URL}/listeners"
C2_LISTENER_CREATE: str = f"{C2_BASE_URL}/listeners"
C2_LISTENER_DELETE: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}"
C2_LISTENER_DETAIL: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}"
C2_LISTENER_UPDATE: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}"
C2_LISTENER_START: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/start"
C2_LISTENER_DEPLOY: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/deploy"
C2_LISTENER_STOP: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/stop"
C2_LISTENER_RESTART: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/restart"
C2_LISTENER_SHELL: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_COMMAND: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_UPLOAD: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_DOWNLOAD: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_DELETE: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_LIST: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell"
C2_LISTENER_SHELL_DETAIL: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell/{shell_id:uuid}"
C2_LISTENER_SHELL_UPDATE: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell/{shell_id:uuid}"
C2_LISTENER_SHELL_START: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell/{shell_id:uuid}/start"
C2_LISTENER_SHELL_STOP: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell/{shell_id:uuid}/stop"
C2_LISTENER_SHELL_RESTART: str = f"{C2_BASE_URL}/listeners/{listener_id:uuid}/shell/{shell_id:uuid}/restart"

C2_IMPLANT_LIST: str = f"{C2_BASE_URL}/implants"
C2_IMPLANT_TYPES_LIST: str = f"{C2_BASE_URL}/implant-types"
