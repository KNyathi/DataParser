import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import VacancyList from './components/VacancyList';
import ApplicantList from './components/ApplicantList';
import { AppBar, Toolbar, Typography, Button, Container } from '@mui/material';

const App = () => (
  <Router>
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Data Parser Portal
        </Typography>
        <Button color="inherit" component={Link} to="/vacancies">Vacancies</Button>
        <Button color="inherit" component={Link} to="/applicants">Applicants</Button>
      </Toolbar>
    </AppBar>
    <Container>
      <Routes>
        <Route path="/vacancies" element={<VacancyList />} />
        <Route path="/applicants" element={<ApplicantList />} />
      </Routes>
    </Container>
  </Router>
);

export default App;
