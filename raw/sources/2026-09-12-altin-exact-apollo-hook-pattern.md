# Altin exact Apollo hook pattern correction

Date: 2026-09-12
Source: Direct user messages in the Altin Partner Mobile Codex conversation.

## Direct instruction

> look at the the query and mutations hooks well:

The user supplied Customers and Menu Products query hooks and Add Customer and Add Employee mutation hooks from their other projects, then asked:

> and what the queries and mutations you wrote in this project does it tally and does it look like how I do my things

After the assistant acknowledged differences, the user explicitly instructed:

> then fucking update them to how I write them, those ones I copied for you is from my other projects that I told you are available for you to always reference and for god sake I have obsidian which has everything and still you go ahead and do what you like. and why you keep putting multiple queries in 1 hook change all that

The user illustrated the rejected implementation with exported ORDERS_OVERVIEW_QUERY, which queried orders three times under pending, confirmed and recent aliases in one MobileOrdersOverview operation.

## Supplied example excerpts

Formatting below removes chat quoting/escape artifacts; identifiers and logic are from the user's supplied examples. These are excerpts, not a new proposed implementation.

```ts
const CustomersGql = gql`
  query GetCustomers($filters: CustomersFilters!) {
    getCustomers(filters: $filters) {
      edges {
        id
        type
        displayName
        companyName
        firstName
        lastName
        email
        phoneNumber
        createdAt
        updatedAt
      }
      pageInfo {
        page
        total
        limit
        hasNextPage
      }
    }
  }
`;

export const useCustomersQuery = (filters: CustomersListFilters = {}) => {
  const { organizationId } = useAppMode();
  const { facilityId } = useFacilityTableFilter();
  const { data, ...result } = useQuery<
    { getCustomers: CustomerConnection },
    { filters: CustomersFilters }
  >(CustomersGql, {
    variables: { filters: { ...filters, facilityId, organizationId: organizationId! } },
    fetchPolicy: "network-only",
    notifyOnNetworkStatusChange: true,
  });
  const customers = useMemo(() => data?.getCustomers.edges || [], [data]);
  const pageInfo = useMemo(() => data?.getCustomers.pageInfo, [data]);
  const showErrorAlert = useMemo(() => !result.loading && result.error, [result]);
  const showNoDataAlert = useMemo(
    () => !customers.length && !result.loading && !result.error,
    [customers, result]
  );
  return { customers, pageInfo, showErrorAlert, showNoDataAlert, ...result };
};
```

The Menu Products example uses `useQuery<Pick<Query, "getProducts">, QueryGetProductsArgs & { facilityId: string }>` and returns named menuItems, pageInfo, display flags and `...result`.

```ts
const addCustomerGQL = gql`
  mutation CreateCustomer($data: CreateCustomerInput!) {
    createCustomer(data: $data) { id }
  }
`;

export const useAddCustomerMutation = () => {
  const [mutate, results] = useMutation<
    { createCustomer: Mutation["createCustomer"] },
    MutationCreateCustomerArgs
  >(addCustomerGQL, { refetchQueries: ["GetCustomers"] });
  const addCustomer = async (data: CreateCustomerInput) => {
    try {
      const results = await mutate({ variables: { data } });
      showNotification({ title: "Success", message: "Customer added successfully", color: "green" });
      return results.data?.createCustomer;
    } catch (error: unknown) {
      showNotification({ title: "Error", color: "red", message: getErrorMessage(error, "An error occurred while adding customer") });
    }
  };
  return { addCustomer, ...results };
};
```

The Add Employee example uses the same structure with generated employee input/args, GetEmployees refetching and employee success/error messages.

## Evidence boundary

The user explicitly authorized updating all mismatching hooks and removing combined aliased overview requests. They did not approve the assistant's earlier gql-relocation or resource-engine approaches. Native notification presentation and backend response-envelope handling require platform/API adaptation; such adaptations are implementation choices, not additional user instructions. Code changes or passing offline tests are not evidence of user acceptance.
