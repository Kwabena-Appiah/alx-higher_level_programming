U
    �UYa�  �                   @   s<   d Z ddlZed�jZG dd� dej�Zedkr8e��  dS )zUnittest for max_integer([..])
�    N�6-max_integerc                   @   sp   e Zd ZdZdd� Zdd� Zdd� Zdd	� Zd
d� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� ZdS )�TestMaxIntegerzunittest class for max_integerc                 C   s    t d�j}| �t|�dk� dS )zTests for module docstingr   �   N)�
__import__�__doc__�
assertTrue�len��self�m� r   �b/root/alx-higher_level_programming/0x07-python-test_driven_development/tests/6-max_integer_test.py�test_module_docstring
   s    
z$TestMaxInteger.test_module_docstringc                 C   s   t j}| �t|�dk� dS )zTests for funstion docstringr   N)�max_integerr   r   r   )r
   �fr   r   r   �test_function_docstring   s    z&TestMaxInteger.test_function_docstringc                 C   s   g }| � t|�� dS )zTests for empty list []N��assertIsNoner   �r
   �er   r   r   �test_empty_list   s    zTestMaxInteger.test_empty_listc                 C   s   | � t� � dS )z%Tests for no arguments passed to funcNr   �r
   r   r   r   �test_no_args   s    zTestMaxInteger.test_no_argsc                 C   s   dg}| � t|�d� dS )z%Tests for only one number in the listr   N��assertEqualr   )r
   �or   r   r   �test_one_element   s    zTestMaxInteger.test_one_elementc                 C   s$   ddddddg}| � t|�d� dS )z&Tests for all positive with max at end�   �
   �   �$   �   �2   Nr   r   r   r   r   �test_positive_end"   s    z TestMaxInteger.test_positive_endc                 C   s$   ddddddg}| � t|�d� dS )z)Tests for all positive with max in middler   r   r   ih  r!   r"   Nr   r	   r   r   r   �test_positive_middle'   s    z#TestMaxInteger.test_positive_middlec                 C   s$   ddddddg}| � t|�d� dS )z,Tests for all positive with max at beginning��   r   r   r    r!   r"   Nr   )r
   �br   r   r   �test_positive_beginning,   s    z&TestMaxInteger.test_positive_beginningc                 C   s$   ddddddg}| � t|�d� dS )z'Tests for list with one negative numberr%   r   r   i����r!   r"   Nr   )r
   Zonr   r   r   �test_one_negative1   s    z TestMaxInteger.test_one_negativec                 C   s"   dddddg}| � t|�d� dS )z(Tests for list with all negative numbersi����i����i���������i����Nr   )r
   �nr   r   r   �test_all_negative6   s    z TestMaxInteger.test_all_negativec              	   C   s"   | � t�� td� W 5 Q R X dS )z"Tests for passing none as argumentN��assertRaises�	TypeErrorr   r   r   r   r   �	test_none;   s    zTestMaxInteger.test_nonec              	   C   s0   dddddg}| � t�� t|� W 5 Q R X dS )z Tests for a non-int type in listr   r   ZHello�   �   Nr,   )r
   �stringr   r   r   �test_non_int_arg@   s    zTestMaxInteger.test_non_int_argN)�__name__�
__module__�__qualname__r   r   r   r   r   r   r#   r$   r'   r(   r+   r/   r3   r   r   r   r   r      s   r   �__main__)r   Zunittestr   r   �TestCaser   r4   �mainr   r   r   r   �<module>   s
   
>