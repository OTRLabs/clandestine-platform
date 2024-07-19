from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .chat import Chat
    from .user import User

class ChatMessage(UUIDAuditBase):
    __tablename__ = 'chat_message'
    __table_args__ = {'comment': 'Chat messages'}
    __pii_columns__ = ['message']
    
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey('chat.id'), nullable=False, comment='Chat ID')
    chat_message_content: Mapped[str] = mapped_column(String(25500), nullable=False, comment='Markdown formatted message content')
    chat_message_sent_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment='Time message was sent')
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False, comment='Sender ID')
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False, comment='Recipient ID')
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='Whether the message has been read')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment='Whether the message has been deleted')
    
    sender: Mapped[User] = relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    recipient: Mapped[User] = relationship('User', foreign_keys=[recipient_id], backref='received_messages')
    chat: Mapped[Chat] = relationship('Chat', backref='messages')
