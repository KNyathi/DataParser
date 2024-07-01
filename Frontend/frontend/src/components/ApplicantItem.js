import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const ApplicantItem = ({ applicant }) => (
  <Card style={{ margin: '20px 0' }}>
    <CardContent>
      <Typography variant="h5">{applicant.title}</Typography>
      <Typography variant="body2"><strong>Age:</strong> {applicant.age}</Typography>
      <Typography variant="body2"><strong>Status:</strong> {applicant.status}</Typography>
      <Typography variant="body2"><strong>Experience Duration:</strong> {applicant.experience_duration}</Typography>
      <Typography variant="body2"><strong>Last Employer:</strong> {applicant.last_employer}</Typography>
      <Typography variant="body2"><strong>Last Position:</strong> {applicant.last_position}</Typography>
      <Typography variant="body2"><strong>Employment Dates:</strong> {applicant.employment_dates}</Typography>
      <Typography variant="body2"><a href={applicant.link} target="_blank" rel="noopener noreferrer">Resume Link</a></Typography>
    </CardContent>
  </Card>
);

export default ApplicantItem;
