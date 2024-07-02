import React from 'react';
import { render, screen } from '@testing-library/react';
import Analytics from './Analytics';

test('renders analytics component and checks for content', () => {
  render(<Analytics />);
  expect(screen.getByText(/We have/i)).toBeInTheDocument();
});
