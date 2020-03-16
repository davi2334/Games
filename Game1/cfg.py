'''config file'''
import os


# FPS
FPS = 100
# Tamanho da tela
SCREENSIZE = (640, 480)
# Caminho da imagem do jogo
IMAGE_PATHS = {
                'rabbit': os.path.join(os.getcwd(), 'resources/images/dude.png'),
                'grass': os.path.join(os.getcwd(), 'resources/images/grass.png'),
                'castle': os.path.join(os.getcwd(), 'resources/images/castle.png'),
                'arrow': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
                'badguy': os.path.join(os.getcwd(), 'resources/images/badguy.png'),
                'healthbar': os.path.join(os.getcwd(), 'resources/images/healthbar.png'),
                'health': os.path.join(os.getcwd(), 'resources/images/health.png'),
                'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
                'youwin': os.path.join(os.getcwd(), 'resources/images/youwin.png')
            }
# Caminho do som do jogo
SOUNDS_PATHS = {
                'hit': os.path.join(os.getcwd(), 'resources/audio/explode.wav'),
                'enemy': os.path.join(os.getcwd(), 'resources/audio/enemy.wav'),
                'shoot': os.path.join(os.getcwd(), 'resources/audio/shoot.wav'),
                'moonlight': os.path.join(os.getcwd(), 'resources/audio/moonlight.wav')
            }
