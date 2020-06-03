U
    ���^�  �                   @   s�   d dl Z d dlZd dlmZ e �d� dadgad�d�ZdZ	d	d
� Z
e
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Ze�  dS )�    N)�Thread�clear�   � uq  [37m
 InvertedOnes       Vk:@inv_ones[32m
 ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃  ┃  ┃  ┓  ┣━┓ ┏━┫  ━━━┫  ━━━┫
 ┗┓   ┏┫  ┗  ┃ ┃ ┃ ┃  ━━━╋━━━  ┃
  ┗━━━┛┗━━━━━┛ ┗━┛ ┗━━━━━┻━━━━━┛
[00m�
u#  Команда для запуска:[33m cd ~/Votes && python votes.py[00m
Эта программа автоматизирует процесс голосования с использованием ваших аккаунтов. Для использования программы необходимо для начала добавить токены от аккаунтов, с которых будет отданы голоса. Взять необходимый токен можно на сайте [36mhttps://vkhost.github.io/[00m, выбрав приложение Kate Mobile. Инструкция по получению токена находится внизу страницы сайта. После получения вы можете добавить токены по одному в базу программы, выбрав опцию Add token (3)
ᅠ
[37m[1] Add votes
[37m[2] Delete votes
ᅠ
[35m[3] Add token[00m
ᅠ
Добавив ваши аккаунты, вы можете приступать к голосованию. Для этого выберите Add votes (1)
ᅠ
[35m[1] Add votes
[37m[2] Delete votes
ᅠ
[37m[3] Add token[00m
ᅠ
После этого программа запросит ссылку на голосование. [31mВнимание![00m Нужна ссылка именно на голосование, не на пост в котором оно размещено. Правильная ссылка выглядит так: https://vk.com/poll*
ᅠ
[35mEnter the link:[00m
ᅠ
После этого выведутся варианты ответов, останется лишь выбрать номер нужного вам
Существует также функция для того, чтобы убрать голоса ваших аккаунтов - Delete votes (2)
ᅠ
[37m[1] Add votes
[35m[2] Delete votes
ᅠ
[37m[3] Add token[00m
ᅠ
По всем вопросам вы можете писать в сообщения группы ВКонтакте [36mhttps://vk.com/inv_ones/c                  C   s^   d} g }t D ]:}|dkr(|�| � d} q| |7 } |dkr|�| � d} q| dkrZ|�| � |S )Nr   � r   )�essay�append)�word�words�char� r   �
nreadme.py�spilit.   s    


r   c              	   C   s.  d}| }t D �]}|t|�|�d�d  |�d� kr�|d dkrz||d d� d|t|�|�d�d  d    7 }d}n"||7 }|t|�|�d�d  8 }nr|d| 7 }|d dkr�||d d� d| t|�|�d�d  d    7 }d}n"||7 }| t|� |�d�d  }|dkr|d7 }|d8 }q|S )	Nr   ��   r   �����r   r   r   )r   �len�count)�width�text�leftr
   r   r   r   �alignB   s&    
$22
r   c                 C   s�   d}t D ]x}d}|d dkr4|dd � }|d d� }|d|   }||d | � 7 }t|�rx|d dkrx||| | d � 7 }||7 }q|S )Nr   �����r   r   r   r   )�banner_linesr   )r   �string�line�tailZ
additionalr   r   r   �banner\   s    
r   c                 C   s�   t t�d |  t t� }t|�}|| dkr4|d7 }| | }dd| td   d d| |t t�d     d d| t t�t   S )Nr   r   z[40mr   �[0mu   █)r   �pages�int�page)r   �floatZintegerZspacer   r   r   �sliderk   s    r$   c                 C   s   d|  S )Nz[Fr   )r   r   r   r   �upt   s    r%   c                  C   s  g } t �dd��� �� }| |k�r�ttt�kr8td8 aq"|} t|d �}t|d �}t|�}g ad| }|t|� dkr�|t|�tt	� d  }n|t|�tt	� d  }|| }|dk�r�t|�|�
d	�d
  |k �r6t|�|�
d	� | }|t|� dk�r|d| |t|� d  7 }n|d| |t|�  7 }d}d}	|d || � �
d	�|	k�r||d || � �
d	�}	|	d
 }�q>t�|d || � d|  � ||| d � }q�t �d� ttt�k�r�td8 a�q�tt|�d||d  | d   d � tt|�t|� d � ttd�t|� ttd   d � td�D �]�}
t �dd��� �� }| |k�r�ttt�k�rztd8 a�q`|} t|d �}t|d �}t|�}g ad| }|t|� dk�r�|t|�tt	� d  }n|t|�tt	� d  }|| }|dk�r�t|�|�
d	� |k �rvt|�|�
d	� | }|t|� dk�r^|d| |t|� d  7 }n|d| |t|�  7 }d}d}	|d || � �
d	�|	k�r�|d || � �
d	�}	|	d
 }�q~t�|d || � d|  � ||| d � }�q�t �d�  �q�t�d� �q<�q�d S )Nz	stty size�rr   r   �   �   �   r   r   r   r   r   u&   Ctrl+Z - выход Enter - далееr   z[00m�   g-C��6?)�os�popen�read�splitr"   r   r    r!   r   r   r   r	   �system�printr%   r$   r   �range�time�sleep)Zdefault_res�resr   Zheightr   r#   Z
free_linesZfreeZlength�literals�ir   r   r   �mainx   s�    



($


r7   c                   C   s2   t �  ttd�� ttt�kr$daq td7 aq d S )Nr(   r   )�inputr0   r%   r"   r   r    r   r   r   r   �inp�   s
    r9   c                   C   s"   t td���  t tdd���  d S )N)�targetT)r:   Zdaemon)r   r7   �startr9   r   r   r   r   �threads�   s    r<   )r+   r2   Z	threadingr   r/   r"   r    r.   r   r   r   r   r   r   r$   r%   r7   r9   r<   r   r   r   r   �<module>   s$   
�	Q