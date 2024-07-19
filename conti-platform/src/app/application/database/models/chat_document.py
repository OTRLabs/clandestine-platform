from __future__ import annotations


from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .document import Document

class ChatDocument(UUIDAuditBase):
    '''A document / file sent in a chat.'''
    __tablename__ = 'chat_document'
    __table_args__ = {'comment': 'Chat documents'}
    __pii_columns__ = ['document_name']
    
    chat_document_name: Mapped[str] = mapped_column(String(255), nullable=False, comment='Document name')
    chat_document_content: Mapped[str] = mapped_column(String(25500), nullable=False, comment='Markdown formatted document content')
    chat_document_sent_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment='Time document was sent')
    chat_document: Mapped[Document] = mapped_column(Integer, ForeignKey('document.id'), nullable=False, comment='Document ID')
    chat_document_url: Mapped[str] = mapped_column(String(255), nullable=False, comment='URL to document')