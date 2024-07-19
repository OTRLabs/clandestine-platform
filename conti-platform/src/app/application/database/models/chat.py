from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .chat_message import ChatMessage
    from .user import User

class Chat(UUIDAuditBase):
    __tablename__ = 'chat'
    __table_args__ = {'comment': 'Chat rooms'}
    __pii_columns__ = ['name']
    
    chat_name: Mapped[str] = mapped_column(String(255), nullable=False, comment='Chat name')
    chat_description: Mapped[str] = mapped_column(String(255), nullable=True, comment='Chat description')
    chat_messages: Mapped[List[ChatMessage]] = relationship('ChatMessage', back_populates='chat', lazy='selectin', uselist=True, cascade='all, delete')
    chat_message_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment='Number of messages in chat')
    chat_members: Mapped[List[User]] = relationship('User', secondary='chat_member', back_populates='chats', lazy='selectin', uselist=True, cascade='all, delete')
    chat_member_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment='Number of members in chat')