from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .chat import Chat
    

class ChatMessage(UUIDAuditBase):
    __tablename__ = 'chat_message'
    __table_args__ = {'comment': 'Chat messages'}
    __pii_columns__ = ['message']
    
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey('chat.id'), nullable=False, comment='Chat ID')
    chat_message_content: Mapped[str] = mapped_column(String(25500), nullable=False, comment='Markdown formatted message content')
    chat_message_sent_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment='Time message was sent')
    