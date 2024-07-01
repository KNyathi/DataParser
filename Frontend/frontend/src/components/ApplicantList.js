import React, { useState, useEffect } from 'react';
import ApplicantItem from './ApplicantItem';
import { TextField, Container, Grid, Paper, Typography } from '@mui/material';
import axios from 'axios';
import useStyles from './styles';
import Analytics from './Analytics';

const ApplicantList = () => {
  const classes = useStyles();
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
    <Container className={classes.container}>
      <Analytics type="applicants" />
      <Typography variant="h4" className={classes.heading}>Applicants</Typography>
      <Grid container spacing={2} className={classes.filterContainer}>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Name" name="title" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Age" name="age" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Status" name="status" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Experience Duration" name="experience_duration" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Last Employer" name="last_employer" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Last Position" name="last_position" onChange={handleFilterChange} />
        </Grid>
      </Grid>
      <Grid container spacing={3} className={classes.listContainer}>
        {applicants.map(applicant => (
          <Grid item xs={12} sm={6} md={4} key={applicant.id}>
            <Paper className={classes.paper}>
              <ApplicantItem applicant={applicant} />
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default ApplicantList;
