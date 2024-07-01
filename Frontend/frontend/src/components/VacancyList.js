import React, { useState, useEffect } from 'react';
import VacancyItem from './VacancyItem';
import { TextField, Container } from '@mui/material';
import axios from 'axios';

const VacancyList = () => {
  const [vacancies, setVacancies] = useState([]);
  const [filter, setFilter] = useState({
    title: '',
    compensation: '',
    experience: '',
    employer: '',
    location: ''
  });

  useEffect(() => {
    axios.get('http://localhost:8000/api/vacancies/', { params: filter })
      .then(response => setVacancies(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, [filter]);

  const handleFilterChange = (e) => {
    setFilter({
      ...filter,
      [e.target.name]: e.target.value
    });
  };

  return (
    <Container>
      <h2>Vacancies</h2>
      <div className="filters">
        <TextField label="Job Title" name="title" onChange={handleFilterChange} />
        <TextField label="Compensation" name="compensation" onChange={handleFilterChange} />
        <TextField label="Experience" name="experience" onChange={handleFilterChange} />
        <TextField label="Employer" name="employer" onChange={handleFilterChange} />
        <TextField label="Location" name="location" onChange={handleFilterChange} />
      </div>
      <div className="vacancy-list">
        {vacancies.map(vacancy => (
          <VacancyItem key={vacancy.id} vacancy={vacancy} />
        ))}
      </div>
    </Container>
  );
};

export default VacancyList;
