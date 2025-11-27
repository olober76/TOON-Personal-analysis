from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Response_Body(BaseModel):
    input_data1: Optional[Dict[str, Any]] = None
    input_data2: Optional[Dict[str, Any]] = None
    input_data3: Optional[Dict[str, Any]] = None