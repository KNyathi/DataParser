import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Applicants from './components/Applicants';
import Vacancies from './components/Vacancies';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/applicants" component={Applicants} />
                <Route path="/vacancies" component={Vacancies} />
            </Switch>
        </Router>
    );
}

export default App;
