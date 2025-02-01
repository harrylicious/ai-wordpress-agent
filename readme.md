# CrewAI WordPress Article Generator

An automated content creation system that generates SEO-optimized, casual-friendly articles and publishes them directly to WordPress. The system uses CrewAI to orchestrate multiple AI agents that handle different aspects of the content creation pipeline.

![image.png](scheme.png)

## 🌟 Features

- Trend analysis and research
- SEO-optimized content creation
- Casual and friendly writing style
- Multi-language support with cultural adaptation
- Automated WordPress publishing
- Modular agent-based architecture

## 📋 Prerequisites

- Python 3.8+
- WordPress installation with REST API enabled
- SerperDev API key for research
- WordPress admin credentials

## 🔧 Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd crewai-wordpress-generator
```

2. Install required packages:

```bash
pip install crewai crewai-tools python-dotenv requests
```

3. Set up your environment variables in a `.env` file:

```env
WORDPRESS_URL=your_wordpress_site_url
WORDPRESS_USERNAME=your_admin_username
WORDPRESS_PASSWORD=your_admin_password
SERPER_API_KEY=your_serper_api_key
```

## 🚀 Usage

```python
from crew_logic import create_crew

# Create a new crew instance
crew = create_crew(
    topic="your topic",
    language_code="target_language_code"  # e.g., "es" for Spanish
)

# Run the content creation pipeline
result = crew.kickoff()
```

## 🤖 Agent Roles

1. **Trend Analyst**

   - Researches current trends
   - Identifies viral content opportunities
   - Analyzes audience interests

2. **Content Creator**

   - Writes engaging, casual content
   - Uses conversational tone
   - Incorporates storytelling elements

3. **SEO Specialist**

   - Optimizes content for search engines
   - Maintains readability
   - Implements keyword strategy

4. **Language Adapter**

   - Translates content
   - Adapts cultural references
   - Maintains tone across languages

5. **Content Publisher**
   - Formats content for WordPress
   - Handles meta information
   - Manages publication process

## 📝 Task Workflow

1. Trend Analysis

   - Research current trends
   - Identify viral angles
   - Gather key insights

2. Content Creation

   - Write engaging content
   - Maintain casual tone
   - Include relatable examples

3. SEO Optimization

   - Integrate keywords
   - Structure content
   - Add meta information

4. Translation

   - Translate content
   - Adapt cultural elements
   - Preserve SEO value

5. Publishing
   - Format content
   - Set up meta data
   - Publish to WordPress

## 🛠️ Tools Used

- `WordPressUploadTool`: Handles WordPress REST API interactions
- `SerperDevTool`: Provides search and research capabilities

## 📁 Project Structure

```
crewai-wordpress-generator/
├── crew_logic.py          # Main crew and agent definitions
├── tools/
│   └── wordpress_upload_tool.py  # WordPress interaction tool
├── .env                   # Environment variables
└── README.md             # This file
```

## ⚙️ Configuration

The system can be configured through environment variables:

- `WORDPRESS_URL`: Your WordPress site URL
- `WORDPRESS_USERNAME`: WordPress admin username
- `WORDPRESS_PASSWORD`: WordPress admin password
- `SERPER_API_KEY`: SerperDev API key for research

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- Ensure your WordPress REST API is properly configured
- Keep your API keys and credentials secure
- Monitor your API usage to stay within limits
- Test translations before production use

## 🐛 Troubleshooting

Common issues and solutions:

1. WordPress API Connection:

   - Verify WordPress REST API is enabled
   - Check credentials in .env file
   - Ensure proper permissions are set

2. Content Generation:

   - Monitor agent outputs for errors
   - Verify API keys are valid
   - Check language code format

3. Publishing Issues:
   - Verify WordPress user permissions
   - Check post status settings
   - Monitor WordPress error logs

## 🔄 Updates and Maintenance

- Regularly update dependencies
- Monitor CrewAI version changes
- Keep API keys current
- Review WordPress compatibility

For additional support or questions, please open an issue in the repository.
