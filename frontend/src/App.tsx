import { RouterProvider } from 'react-router-dom';
import router from './routes';
import { Button, useColorMode } from '@chakra-ui/react';

function ColorModeSwitcher() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Button position="fixed" top="4" right="4" onClick={toggleColorMode}">
      {colorMode === 'light' ? 'Dark' : 'Light'}
    </Button>
  );
}

function App() {
  return (
    <>
      <ColorModeSwitcher />
      <RouterProvider router={router} />
    </>
  );
}

export default App;
