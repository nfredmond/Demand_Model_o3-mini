import React, { useState } from 'react';
import { uploadFile } from '../api';

const DataUploadComponent: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    try {
      await uploadFile(file);
      alert('File uploaded successfully');
    } catch (error) {
      alert('Upload failed');
    }
  };

  return (
    <div>
      <h3>Upload Geospatial Data</h3>
      <input type="file" onChange={handleFileChange} accept=".kml,.kmz,.shp,.geojson" />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default DataUploadComponent;
