import React from 'react';
import { Card, CardContent, Typography, CardActions, Button } from '@mui/material';
import useStyles from './styles';

const ApplicantItem = ({ applicant }) => {
  const classes = useStyles();
  
  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6" component="div">{applicant.title}</Typography>
        <Typography color="textSecondary">{applicant.status}</Typography>
        <Typography variant="body2" component="p">{applicant.age}</Typography>
        <Typography variant="body2" component="p">{applicant.experience_duration}</Typography>
        <Typography variant="body2" component="p">{applicant.last_employer}</Typography>
        <Typography variant="body2" component="p">{applicant.last_position}</Typography>
      </CardContent>
      <CardActions>
        <Button size="small" color="primary" href={applicant.link} target="_blank">Learn More</Button>
      </CardActions>
    </Card>
  );
};

export default ApplicantItem;
