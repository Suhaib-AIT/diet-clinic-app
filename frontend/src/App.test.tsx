import { render, screen } from '@testing-library/react';
import { ChakraProvider } from '@chakra-ui/react';
import App from './App';
import theme from './theme';

it('renders login page', () => {
  render(
    <ChakraProvider theme={theme}>
      <App />
    </ChakraProvider>
  );
  expect(screen.getByText(/login/i)).toBeInTheDocument();
});
