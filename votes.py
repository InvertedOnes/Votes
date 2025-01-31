U
    �^K  �                B   @   s�  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zee�	dd��
� �� d �ZdZd	d
� Zdd� Zdd� Zed� ed�Zedk�r�ed�Z�ze jed�Ze jeddd�Zeeddddddddddddddddd d!d"d#dd$ddddd!d"dd%d&g�� eeddddd'dd(d(dd)d$ddddd d!dddd"dd%d!d'd"dd$d*dd+d,d-d.d/d0d1d2d3d2d4d.d5dd!ddd*dd+d,d2d5dddddddd,dd6d&g@�� edd7�Ze�ed8 � e��  W n   ed9� Y nX ed:� e�  n(ed;k�r�d<Zned=k�r�ed>� e�  e� Ze�� Zg Zed �Zej j!ed ed? d@�Z"e"dA Z#e"dB Z$e$�rLdZ%nd Z%e"dC Z&e&D ]�Z'e�(e'dD � e'dD e#k�r�dEZ)dFZ*ndGZ)dHZ*ee*� e+e,e��Z-e'dI Z.e+e/e.��dJ Z0e-dKee,e-� e,e0�   e0 Z1e/ee. dL �Z2e1de2� dG e1e2d�  Z1ee1� ee)e'dM  dG � �q\eedN��d Z3ee3 Z4e�  d Z5d Z6ee5�Zed<k�rb�q�z`e�r�ej j7ed ed? e4e%dO� nej j8ed ed? e4e%dO� e6d7 Z6edPe+e6� dQ � W n   edR� Y nX e5d7 Z5�qLe�  dS )S�    N�clearz.tokensza+�rz	stty size�   Fc                 C   s*   d}| D ]}|t t|d d ��7 }q|S )N� �   g      �?)�chr�int)Zmassive�str�n� r   �votes.py�dec   s    r   c                 C   sL   | t t�krdS t|  }|d t |�d � }tj|d�}tj|ddd�S d S )NTr   �Zaccess_token�5.89�ru��vZlang)�len�tokens�vk�Session�API)�dow�token�sessionr   r   r   �login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dkr�td
� t�  |||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger   r   �print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r(   u�  [37m
 InvertedOnes      Vk: @inv_ones[32m
 ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃  ┃  ┃  ┓  ┣━┓ ┏━┫  ━━━┫  ━━━┫
 ┗┓   ┏┫  ┗  ┃ ┃ ┃ ┃  ━━━╋━━━  ┃
  ┗━━━┛┗━━━━━┛ ┗━┛ ┗━━━━━┻━━━━━┛
[35m
[1] Add votes
[2] Delete votes

[3] Add token
z&Please, enter your task's number: [0m�3z[35mEnter the token: [0mr   r   r   r   i�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �a�
z
[31mInvalid tokenr   �2T�1z
[31mInvalid task's number
r    )�owner_id�poll_id�
answer_ids�is_board�answers�idz[36mz[46mz[0mz[41m�rate�%� �d   �textz
[35mYour choice: [0m)r.   r/   r0   r1   z[32mSuccessful (�)z
[31mError)9r   �time�os�system�open�w�close�fr   �popen�read�split�widthZfor_delr   r   r(   r#   r!   ZtaskZtkr   r   r   Zapi�exec�writer$   Z	parametrs�	readlinesr   ZidsZpollsZgetByIdZpollZ
my_answersr1   Zis_bintr2   Zanswer�appendZcolorZ
line_colorr	   r   ZnumZpercent�roundr4   �lineZedgeZchoice�targetr   ZsuccZ
deleteVoteZaddVoter   r   r   r   �<module>   s�   


	"
J�


 
