import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const VacancyItem = ({ vacancy }) => (
  <Card style={{ margin: '20px 0' }}>
    <CardContent>
      <Typography variant="h5">{vacancy.title}</Typography>
      <Typography variant="subtitle1">{vacancy.employer}</Typography>
      <Typography variant="body2">{vacancy.location}</Typography>
      <Typography variant="body2"><strong>Compensation:</strong> {vacancy.compensation}</Typography>
      <Typography variant="body2"><strong>Experience:</strong> {vacancy.experience}</Typography>
      <Typography variant="body2"><a href={vacancy.link} target="_blank" rel="noopener noreferrer">Job Link</a></Typography>
    </CardContent>
  </Card>
);

export default VacancyItem;
