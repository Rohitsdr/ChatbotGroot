# Groot Chatbot #

A stunning anime-style chatbot built with Streamlit featuring modern UI design, API integration, and interactive chat functionality.

## ✨ Features

- **Anime-Style UI**: Beautiful gradient backgrounds, animated elements, and kawaii design
- **Real-time Chat**: Interactive chat interface with message bubbles and animations
- **API Integration**: Connect to OpenAI or any compatible API service
- **Customizable**: Configurable API settings, temperature, and max tokens
- **Quick Actions**: Pre-built conversation starters
- **Responsive Design**: Works on desktop and mobile devices
- **Loading Animations**: Smooth loading indicators and transitions

## 🚀 Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd ChatbotGroot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 🛠️ Configuration

### API Setup

1. **OpenAI API** (Recommended):
   - Get your API key from [OpenAI](https://platform.openai.com/api-keys)
   - Enter the API key in the sidebar
   - Default endpoint: `https://api.openai.com/v1/chat/completions`

2. **Custom API**:
   - Set your custom API endpoint in the sidebar
   - Configure authentication as needed
   - Ensure your API follows OpenAI-compatible format

### Settings

- **Temperature**: Controls response randomness (0.0 = deterministic, 2.0 = very random)
- **Max Tokens**: Maximum length of AI responses
- **Theme**: Visual theme selection (coming soon)

## 💬 Usage

1. **Start the app**: Run `streamlit run main.py`
2. **Configure API**: Enter your API key in the sidebar
3. **Start chatting**: Type your message and press "Send 🚀"
4. **Use quick actions**: Click pre-built buttons for common requests
5. **Clear chat**: Use the "Clear Chat" button to start fresh

## 🎨 UI Features

- **Animated Header**: Gradient background with bouncing title
- **Chat Bubbles**: Styled message bubbles with slide-in animations
- **Loading Indicators**: Smooth loading animations while processing
- **Responsive Layout**: Adapts to different screen sizes
- **Modern Design**: Clean, anime-inspired aesthetics

## 📱 Quick Actions

- **🎨 Tell me a story**: Get an anime-style story
- **🤖 Explain AI**: Learn about artificial intelligence
- **🌸 Anime Facts**: Discover interesting anime facts
- **🎭 Random Joke**: Get a funny joke

## 🔧 Technical Details

- **Framework**: Streamlit
- **Styling**: Custom CSS with animations
- **API**: REST API integration with error handling
- **State Management**: Streamlit session state
- **Dependencies**: streamlit, requests, typing-extensions

## 🌟 Demo Mode

The app includes a demo mode that works without an API key. It will return sample responses to test the UI and functionality.

## 🔒 Security

- API keys are handled securely using Streamlit's password input
- No sensitive data is stored locally
- All API calls are made over HTTPS

## 🎯 Future Enhancements

- Multiple theme options
- Voice input/output
- File upload support
- Export chat history
- Custom persona settings
- Multi-language support

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the chatbot!

## 📞 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

Made with ❤️ by Anime Groot | Powered by Streamlit ✨ 
