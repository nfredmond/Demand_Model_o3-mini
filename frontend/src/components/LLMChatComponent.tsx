import React, { useState } from 'react';
import { askLLM } from '../api';

const LLMChatComponent: React.FC = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleQuery = async () => {
    try {
      const res = await askLLM(query);
      setResponse(res.data.answer);
    } catch (error) {
      setResponse('Error: Could not get response');
    }
  };

  return (
    <div>
      <h3>Ask the AI</h3>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
      <button onClick={handleQuery}>Ask</button>
      <p>{response}</p>
    </div>
  );
};

export default LLMChatComponent;
