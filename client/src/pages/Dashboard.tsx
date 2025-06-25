import {
  Box,
  Button,
  Heading,
  SimpleGrid,
  Stat,
  StatLabel,
} from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';

type Props = {
  user: string;
};

const Dashboard = ({ user }: Props) => {
  return (
    <Box p={4}>
      <Heading size="lg" mb={6}>{`Hi, ${user}!`}</Heading>
      <SimpleGrid columns={{ base: 1, md: 2 }} spacing={4} mb={6}>
        <Stat p={4} borderWidth="1px" borderRadius="md">
          <StatLabel>Upcoming Appointments</StatLabel>
        </Stat>
        <Stat p={4} borderWidth="1px" borderRadius="md">
          <StatLabel>Active Diet Plan</StatLabel>
        </Stat>
      </SimpleGrid>
      <Button as={RouterLink} to="/book-appointment" colorScheme="teal">
        Book new appointment
      </Button>
    </Box>
  );
};

export default Dashboard;
