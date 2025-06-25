import { extendTheme, ThemeConfig } from '@chakra-ui/react';

const config: ThemeConfig = {
  initialColorMode: 'light',
  useSystemColorMode: false,
};

const theme = extendTheme({
  config,
  colors: {
    brand: {
      600: '#319795', // teal
    },
    accent: {
      400: '#A3E635', // lime
    },
  },
});

export default theme;
