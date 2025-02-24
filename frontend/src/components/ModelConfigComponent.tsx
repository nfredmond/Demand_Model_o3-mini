import React, { useState } from 'react';
import { runModel } from '../api';
import { useDispatch } from 'react-redux';

const ModelConfigComponent: React.FC = () => {
  const [area, setArea] = useState('');
  const [param1, setParam1] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async () => {
    const config = { project_id: 1, area, param1 }; // Using project_id=1 as an example.
    try {
      const response = await runModel(config);
      dispatch({ type: 'SET_MODEL_RESULTS', payload: response.data });
      alert('Model run initiated');
    } catch (error) {
      alert('Failed to run model');
    }
  };

  return (
    <div>
      <h3>Model Configuration</h3>
      <label>
        Area:
        <input type="text" value={area} onChange={(e) => setArea(e.target.value)} placeholder="e.g., New York" />
      </label>
      <br />
      <label>
        Parameter 1:
        <input type="text" value={param1} onChange={(e) => setParam1(e.target.value)} />
      </label>
      <br />
      <button onClick={handleSubmit}>Run Model</button>
    </div>
  );
};

export default ModelConfigComponent;
