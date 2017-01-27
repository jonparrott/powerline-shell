import os

def add_virtual_env_segment():

    env = os.getenv('VIRTUAL_ENV')
    if env is None:
        return

    env_name = os.path.basename(env)
    env_path = os.path.dirname(env)

    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG

    global_envs = os.path.expanduser('~/venvs')

    if env_path in global_envs:
        show_name = True
        bg = Color.VIRTUAL_ENV_GLOBAL_BG
    else:
        show_name = False
        if env_path not in os.getcwd():
            bg = Color.VIRTUAL_ENV_BAD_BG

    powerline.append(
        u' \u23E3 ' + (env_name if show_name else ''), fg, bg)


add_virtual_env_segment()
