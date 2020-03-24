U
    [z^k  �                   @   s�  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zee�	dd��
� �� d �ZdZd	d
� Zdd� Zed� ed�Zedk�rjed�Zz�e jed�Ze jeddd�Zzejjdd� e�d� W n   dZY nX ejjded� ejjddd�d d  d Zejj ed d� e�d� edd�Ze�!ed � e��  W n   ed � Y nX ed!� e"�  n(ed"k�rzd#Zned$k�r�ed%� e"�  e� Z#e�$� Z%g Z&ed �Zej'j(e#d e#d& d'�Z)e)d( Z*e)d) Z+e+�r�dZ,nd Z,e)d* Z-e-D ]�Z.e&�/e.d � e.d e*k�rd+Z0d,Z1nd-Z0d.Z1ee1� e2e3e&��Z4e.d/ Z5e2e6e5��d0 Z7e4d1ee3e4� e3e7�   e7 Z8e6ee5 d2 �Z9e8de9� d- e8e9d�  Z8ee8� ee0e.d3  d- � �q�eed4��d Z:e&e: Z;e�  d Z<d Z=ee<�Zed#k�r��qxz`e�rej'j>e#d e#d& e;e,d5� nej'j?e#d e#d& e;e,d5� e=d7 Z=ed6e2e=� d7 � W n   ed8� Y nX e<d7 Z<�q�e�  dS )9�    N�clearz.tokensza+�rz	stty size�   Fc                 C   sL   | t t�krdS t|  }|d t |�d � }tj|d�}tj|ddd�S d S )NTr   �Zaccess_token�5.89�ru��vZlang)�len�tokens�vk�Session�API)�dow�token�session� r   �votes.py�login   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dkr�td
� t�  |||fS )Nr   � z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger
   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r#   u�  [37m
 InvertedOnes Vk: @inverted_ones[32m
 ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃  ┃  ┃  ┓  ┣━┓ ┏━┫  ━━━┫  ━━━┫
 ┗┓   ┏┫  ┗  ┃ ┃ ┃ ┃  ━━━╋━━━  ┃
  ┗━━━┛┗━━━━━┛ ┗━┛ ┗━━━━━┻━━━━━┛
[35m
[1] Add votes
[2] Delete votes

[3] Add token
z&Please, enter your task's number: [0m�3z[35mEnter the token: [0mr   r   r   r   i�ϭ)�owner_idg      �?Zpidor)�user_id�message)r&   �count�items�id)Zmessage_idsZdelete_for_all�a�
z
[31mInvalid tokenr   �2T�1z
[31mInvalid task's number
r   )r%   �poll_id�
answer_ids�is_board�answersz[36mz[46mz[0mz[41m�rate�%� �d   �textz
[35mYour choice: [0m)r%   r/   r0   r1   z[32mSuccessful (�)z
[31mError)@r   �time�os�system�open�w�close�fr   �popen�read�split�widthZfor_delr   r#   r   r   ZtaskZtkr   r   r   ZapiZaccountZunban�sleepZyouZmessages�sendZ
getHistoryZmg_id�delete�writer   Z	parametrs�	readlinesr   ZidsZpollsZgetByIdZpollZ
my_answersr1   Zis_bintr2   Zanswer�appendZcolorZ
line_color�strr
   ZnumZpercent�roundr3   �lineZedgeZchoice�targetr   ZsuccZ
deleteVoteZaddVoter   r   r   r   �<module>   s�   


	"





 
