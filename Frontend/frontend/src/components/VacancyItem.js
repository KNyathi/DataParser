import React from 'react';
import { Card, CardContent, Typography, CardActions, Button } from '@mui/material';
import useStyles from './styles';

const VacancyItem = ({ vacancy }) => {
  const classes = useStyles();
  
  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6" component="div">{vacancy.title}</Typography>
        <Typography color="textSecondary">{vacancy.employer}</Typography>
        <Typography variant="body2" component="p">{vacancy.location}</Typography>
        <Typography variant="body2" component="p">{vacancy.experience}</Typography>
        <Typography variant="body2" component="p">{vacancy.compensation}</Typography>
      </CardContent>
      <CardActions>
        <Button size="small" color="primary" href={vacancy.link} target="_blank">Learn More</Button>
      </CardActions>
    </Card>
  );
};

export default VacancyItem;
