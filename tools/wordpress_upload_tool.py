from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
from requests.auth import HTTPBasicAuth

class WordPressPostArgs(BaseModel):
    """Input schema for WordPressUploadTool."""
    title: str = Field(..., description="The title of the WordPress post.")
    content: str = Field(..., description="The content of the WordPress post.")
    status: str = Field(
        default="publish",
        description="The status of the post. Can be 'publish' or 'draft'."
    )

class WordPressUploadTool(BaseTool):
    name: str = "WordPress Post Upload"
    description: str = (
        "Uploads a post to WordPress using the REST API. "
        "Requires WordPress URL, username, and password."
    )
    args_schema: Type[BaseModel] = WordPressPostArgs
    
    wordpress_url: str = Field(..., description="The base URL of your WordPress site")
    username: str = Field(..., description="WordPress username")
    password: str = Field(..., description="WordPress password")

    def __init__(self, **kwargs):
        """
        Initializes the WordPressUploadTool with the necessary credentials.
        
        :param kwargs: Dictionary containing wordpress_url, username, and password
        """
        super().__init__(**kwargs)

    def _run(self, title: str, content: str, status: str = "publish") -> str:
        """
        Uploads a post to WordPress using the REST API.
        
        :param title: The title of the post
        :param content: The content of the post
        :param status: The status of the post (publish or draft)
        :return: A string indicating success or failure with details
        """
        endpoint = f"{self.wordpress_url}/wp-json/wp/v2/posts"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "title": title,
            "content": content,
            "status": status
        }
        
        try:
            response = requests.post(
                endpoint,
                json=data,
                headers=headers,
                auth=HTTPBasicAuth(self.username, self.password)
            )
            response.raise_for_status()
            
            return (
                f"Post uploaded successfully!\n"
                f"Post ID: {response.json().get('id')}\n"
                f"Status: {status}"
            )
            
        except requests.exceptions.RequestException as e:
            return f"Failed to upload post: {str(e)}"