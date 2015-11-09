import os

def add_virtual_env_segment():

    env = os.getenv('VIRTUAL_ENV')
    if env is None:
        return

    env_name = os.path.basename(env)
    env_path = os.path.dirname(env)

    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG

    if env_path not in os.getcwd():
        bg = Color.VIRTUAL_ENV_BAD_BG

    powerline.append(u' \u23E3 ', fg, bg)


add_virtual_env_segment()
