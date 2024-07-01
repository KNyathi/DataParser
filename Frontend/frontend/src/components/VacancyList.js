import React, { useState, useEffect } from 'react';
import VacancyItem from './VacancyItem';
import { TextField, Container, Grid, Paper, Typography } from '@mui/material';
import axios from 'axios';
import useStyles from './styles';

const VacancyList = () => {
  const classes = useStyles();
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
    <Container className={classes.container}>
      <Typography variant="h4" className={classes.heading}>Vacancies</Typography>
      <Grid container spacing={2} className={classes.filterContainer}>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Job Title" name="title" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Compensation" name="compensation" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Experience" name="experience" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Employer" name="employer" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Location" name="location" onChange={handleFilterChange} />
        </Grid>
      </Grid>
      <Grid container spacing={3} className={classes.listContainer}>
        {vacancies.map(vacancy => (
          <Grid item xs={12} sm={6} md={4} key={vacancy.id}>
            <Paper className={classes.paper}>
              <VacancyItem vacancy={vacancy} />
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default VacancyList;
