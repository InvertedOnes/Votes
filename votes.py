U
    ��x^�  �                   @   s  d dl Z d dlZd dlZe�d� edd�Ze��  edd�Zee�	dd��
� �� d �Zdd	� Zd
d� Zed� ed�Zedk�rfed�Zz�e jed�Ze jeddd�Zzejjdd� e�d� W n   dZY nX ejjded� ejjddd�d d  d Zejjed d� e�d� edd�Ze� ed � e��  W n   ed� Y nX ed � e!�  ned!k�r~ed"� e!�  e� Z"e�#� Z$g Z%ed �Zej&j'e"d e"d# d$�d% Z(e(D ]�Z)e%�*e)d � ed&� e+e,e%��Z-e)d' Z.e+e/e.��d( Z0e-d)ee,e-� e,e0�   e0 Z1e/ee. d* �Z2e1de2� d+ e1e2d�  Z1ee1� ed+e)d,  � �q�eed-��d Z3e%e3 Z4e�  d Z5d Z6ee5�Zed.k�r��q�z:ej&j7e"d e"d# e4d/� e6d7 Z6ed0e+e6� d1 � W n   � ed2� Y nX e5d7 Z5�q�e�  dS )3�    N�clearz.tokensza+�rz	stty size�   c                 C   sL   | t t�krdS t|  }|d t |�d � }tj|d�}tj|ddd�S d S )NTr   �Zaccess_token�5.89�ru��vZlang)�len�tokens�vk�Session�API)�dow�token�session� r   �votes.py�login	   s    r   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dkr�td
� t�  |||fS )Nr   � z[35mEnter the link: [0m�.�   �-r   �_�   z
[31mInvalid link
)�input�ranger
   �int�print�quit)Zspace�step�typeZfirstIDZsecondIDZlink�charr   r   r   �getlink   s>    r#   u�  [37m
 InvertedOnes Vk: @inverted_ones[32m
 ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃  ┃  ┃  ┓  ┣━┓ ┏━┫  ━━━┫  ━━━┫
 ┗┓   ┏┫  ┗  ┃ ┃ ┃ ┃  ━━━╋━━━  ┃
  ┗━━━┛┗━━━━━┛ ┗━┛ ┗━━━━━┻━━━━━┛
[35m
[1] Add votes
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0mr   r   r   r   i�ϭ)�owner_idg      �?Zpidor)�user_id�message)r&   �count�items�id)Zmessage_idsZdelete_for_all�a�
z
[31mInvalid tokenr   �1z
[31mInvalid task's number
r   )r%   �poll_id�answersz[41m�rate�%� �d   z[0m�textz
[35mYour choice: [0mT)r%   r.   Z
answer_idsz[32mSuccessful (�)z
[31mError)8r   �time�os�system�open�w�close�fr   �popen�read�split�widthr   r#   r   r   ZtaskZtkr   r   r   ZapiZaccountZunban�sleepZyouZmessages�sendZ
getHistoryZmg_id�delete�writer   Z	parametrs�	readlinesr   ZidsZpollsZgetByIdr/   Zanswer�append�strr
   ZnumZpercent�roundr0   �lineZedgeZchoice�targetr   ZsuccZaddVoter   r   r   r   �<module>   s�   


	"





 
