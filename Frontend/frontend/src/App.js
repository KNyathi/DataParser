import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Applicants from './components/Applicants';
import Vacancies from './components/Vacancies';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/applicants" element={<Applicants />} />
                <Route path="/vacancies" element={<Vacancies />} />
            </Routes>
        </Router>
    );
}

export default App;
