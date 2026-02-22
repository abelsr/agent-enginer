from typing import Dict, Any, List, Optional
from datetime import datetime


class Memory:
    """Memory management system for agents."""

    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.short_term: List[Dict[str, Any]] = []
        self.long_term: Dict[str, Any] = {}

    def add(self, item: Dict[str, Any]) -> None:
        """Add an item to memory."""
        item["timestamp"] = datetime.now().isoformat()
        
        if len(self.short_term) >= self.max_size:
            # Move oldest to long-term
            oldest = self.short_term.pop(0)
            key = f"{oldest.get('role', 'unknown')}_{oldest.get('timestamp', '')}"
            self.long_term[key] = oldest
        
        self.short_term.append(item)

    def get_recent(self, n: int = 10) -> List[Dict[str, Any]]:
        """Get the n most recent items."""
        return self.short_term[-n:]

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search memory for items containing query."""
        results = []
        for item in self.short_term:
            if query.lower() in str(item.get("content", "")).lower():
                results.append(item)
        return results

    def clear(self) -> None:
        """Clear all memory."""
        self.short_term.clear()
        self.long_term.clear()

    def get_stats(self) -> Dict[str, int]:
        """Get memory statistics."""
        return {
            "short_term_size": len(self.short_term),
            "long_term_size": len(self.long_term),
            "max_size": self.max_size
        }
