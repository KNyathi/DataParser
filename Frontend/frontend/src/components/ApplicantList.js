import React, { useState, useEffect } from 'react';
import ApplicantItem from './ApplicantItem';
import { TextField, Container } from '@mui/material';
import axios from 'axios';

const ApplicantList = () => {
  const [applicants, setApplicants] = useState([]);
  const [filter, setFilter] = useState({
    title: '',
    age: '',
    status: '',
    experience_duration: '',
    last_employer: '',
    last_position: ''
  });

  useEffect(() => {
    axios.get('http://localhost:8000/api/applicants/', { params: filter })
      .then(response => setApplicants(response.data))
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
      <h2>Applicants</h2>
      <div className="filters">
        <TextField label="Name" name="title" onChange={handleFilterChange} />
        <TextField label="Age" name="age" onChange={handleFilterChange} />
        <TextField label="Status" name="status" onChange={handleFilterChange} />
        <TextField label="Experience Duration" name="experience_duration" onChange={handleFilterChange} />
        <TextField label="Last Employer" name="last_employer" onChange={handleFilterChange} />
        <TextField label="Last Position" name="last_position" onChange={handleFilterChange} />
      </div>
      <div className="applicant-list">
        {applicants.map(applicant => (
          <ApplicantItem key={applicant.id} applicant={applicant} />
        ))}
      </div>
    </Container>
  );
};

export default ApplicantList;
