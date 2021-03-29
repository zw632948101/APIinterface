#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, func, SmallInteger, ForeignKey, Text, \
    table
from sqlalchemy.orm import relationship

Base = declarative_base()
