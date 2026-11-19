import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import './styles.css';
import './brand.css';
import './contact.css';
import './mobile.css';

createRoot(document.getElementById('root')).render(<React.StrictMode><App /></React.StrictMode>);
