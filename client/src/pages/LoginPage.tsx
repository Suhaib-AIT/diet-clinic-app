import { FormEvent, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Input,
  Heading,
  Flex,
} from '@chakra-ui/react';

type Props = {
  onLogin: (user: string) => void;
};

const LoginPage = ({ onLogin }: Props) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    onLogin(username);
    navigate('/dashboard');
  };

  return (
    <Flex minH="100vh" align="center" justify="center">
      <Box as="form" onSubmit={handleSubmit} p={8} borderWidth={1} borderRadius="md" boxShadow="md">
        <Heading mb={6}>Login</Heading>
        <FormControl mb={4}>
          <FormLabel>Username</FormLabel>
          <Input value={username} onChange={(e) => setUsername(e.target.value)} />
        </FormControl>
        <FormControl mb={6}>
          <FormLabel>Password</FormLabel>
          <Input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </FormControl>
        <Button type="submit" colorScheme="teal" width="full">
          Log in
        </Button>
      </Box>
    </Flex>
  );
};

export default LoginPage;
