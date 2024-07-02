import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders App component and checks for content', () => {
  render(<App />);
  expect(screen.getByText(/Welcome to our Job Portal/i)).toBeInTheDocument();
});
