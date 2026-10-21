# Altin Form Layer and Schema Rejection

Date: 2026-09-12
Source: direct user correction and supplied code attachment in the Altin Partner Mobile task.

## Direct user evidence

> all you did is still all the yup and formik stuff are all still wrong and you adding plenty files and folders for nothing, i don't see the reason for this /Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile/src/outlets/outletForm fucking reference serlp oh my God is that too hard to do? wtf, until you fucking structure the codes right we still stuck fuck you

The attached code below is the implementation the user rejected, not an approved template.

## Rejected code supplied by user

```typescript
const measurement = yup
  .string()
  .trim()
  .test(
    "positive",
    "Use positive numbers for parcel measurements.",
    (value) =>
      !value ||
      (/^\d+(\.\d+)?$/.test(value) &&
        Number.isFinite(Number(value)) &&
        Number(value) > 0),
  );
const coordinate = (label: string, limit: number) =>
  yup
    .string()
    .trim()
    .required(`Enter the delivery ${label}.`)
    .matches(/^[+-]?(?:\d+\.?\d*|\.\d+)$/, `Enter a valid delivery ${label}.`)
    .test(
      "range",
      `Enter a delivery ${label} between −${limit} and ${limit}.`,
      (value) =>
        !value ||
        (Number.isFinite(Number(value)) && Math.abs(Number(value)) <= limit),
    );
const orderParcelSchema = yup.object().shape({
  outlet: yup
    .object({ id: yup.string().required("Select a pickup outlet.") })
    .default(undefined)
    .required("Select a pickup outlet."),
  latitude: coordinate("latitude", 90),
  longitude: coordinate("longitude", 180),
  paymentMethod: yup
    .mixed<OrderPaymentMethod>()
    .oneOf([OrderPaymentMethod.CASH, OrderPaymentMethod.INVOICE])
    .required(),
  items: yup
    .array()
    .of(
      yup.object().shape({
        description: yup
          .string()
          .trim()
          .required("Add a parcel description.")
          .max(256),
        quantity: yup
          .string()
          .required("Enter a quantity.")
          .matches(/^\d+$/, "Enter a valid quantity.")
          .test(
            "quantity",
            "Enter a valid quantity.",
            (value) =>
              !value || (Number(value) >= 1 && Number(value) <= 2147483647),
          ),
        estimatedWeightKg: measurement,
        lengthCm: measurement,
        widthCm: measurement,
        heightCm: measurement,
      }),
    )
    .required()
    .min(1, "Include between 1 and 50 items.")
    .max(50, "Include between 1 and 50 items."),
});
const orderDeliverySchema = yup.object().shape({
  contactName: yup
    .string()
    .trim()
    .required("Enter a recipient name.")
    .max(64, "Enter a recipient name up to 64 characters."),
  contactPhone: yup
    .string()
    .trim()
    .required("Enter a Ghana phone number.")
    .matches(
      /^\+233\d{9}$/,
      "Enter a Ghana phone number: +233 followed by 9 digits.",
    ),
  contactEmail: yup.string().trim().email("Enter a valid email address."),
  addressLine1: yup
    .string()
    .trim()
    .required("Enter a delivery address.")
    .max(256, "Enter a delivery address up to 256 characters."),
  orderValue: yup
    .string()
    .trim()
    .when("paymentMethod", {
      is: OrderPaymentMethod.CASH,
      then: (schema) => schema.required("Enter the cash amount to collect."),
    })
    .test(
      "amount",
      "Enter an amount up to 10,000,000 with at most two decimal places.",
      (value) =>
        !value ||
        (/^\d+(\.\d{1,2})?$/.test(value) && Number(value) <= 10000000),
    ),
  deliveryOtp: yup
    .string()
    .trim()
    .matches(/^(\d{4}|\d{6})$/, {
      message: "Delivery OTP must contain 4 or 6 digits.",
      excludeEmptyString: true,
    }),
});
const orderEstimateSchema = orderParcelSchema.shape({
  estimateId: yup.string().required("Choose a delivery option."),
});
const orderValidationSchema = orderEstimateSchema.concat(orderDeliverySchema);

export const useCreateOrderForm = () => {
  const navigation =
    useNavigation<NativeStackNavigationProp<RootStackParamList>>();
  const { currentOrganizationId } = useAuthentication();
  const access = useAppAccess();
  const [initialValues] = useState(emptyOrder);
  const [step, setStep] = useState(0);
  const [estimates, setEstimates] = useState<OrderEstimate[]>([]);
  const [created, setCreated] = useState<CreatedOrder>();
  const organizationAtMount = useRef(currentOrganizationId);
  const { getPriceEstimate, loading: quoting } = useOrderPriceEstimate();
  const { createOrder, loading: creating } = useCreateOrder();
  const live = useRef({
    organizationId: currentOrganizationId,
    allowed: access.createOrders,
  });
  live.current = {
    organizationId: currentOrganizationId,
    allowed: access.createOrders,
  };
  const mounted = useRef(true),
    busy = useRef<Promise<unknown> | undefined>(undefined);
  useEffect(() => {
    mounted.current = true;
    return () => {
      mounted.current = false;
    };
  }, []);
  const form = useFormik<CreateOrderFormValues>({
    initialValues,
    onSubmit: async (values, helpers) => {
      if (busy.current) {
        try {
          await busy.current;
        } catch {
          /* The original submission displays the error. */
        }
        return;
      }
      if (
        created ||
        !currentOrganizationId ||
        !access.createOrders ||
        organizationAtMount.current !== currentOrganizationId
      )
        return;
      helpers.setStatus(undefined);
      const scope = currentOrganizationId;
      const valid = () =>
        mounted.current &&
        live.current.organizationId === scope &&
        live.current.allowed;
      try {
        if (step === 2) {
          if (
            !estimates.some((estimate) => estimate.id === values.estimateId)
          ) {
            helpers.setFieldError(
              "estimateId",
              "Choose a current delivery option.",
            );
            return;
          }
          const request = createOrder(
            createOrderInput(values, values.estimateId),
          );
          busy.current = request;
          const record = await request;
          if (valid()) setCreated(record);
        } else {
          setEstimates([]);
          void helpers.setFieldValue("estimateId", "", false);
          const request = getPriceEstimate(estimateInput(values));
          busy.current = request;
          const data = await request;
          if (valid()) {
            setEstimates(data.estimates);
            setStep(1);
          }
        }
      } catch (e) {
        if (valid())
          helpers.setStatus(
            step === 2
              ? `${errorMessage(e)}\nIf the connection failed after submission, check Delivery Orders before submitting again.`
              : errorMessage(e),
          );
      } finally {
        busy.current = undefined;
      }
    },
    validateOnMount: true,
    validationSchema:
      step === 2
        ? orderValidationSchema
        : step === 1 && estimates.length > 0
          ? orderEstimateSchema
          : orderParcelSchema,
  });
  useEffect(() => {
    void form.validateForm();
  }, [step, estimates.length, form.validateForm]);
  const submitting = form.isSubmitting || quoting || creating;
  usePreventRemove(
    !created &&
      (form.dirty || submitting) &&
      organizationAtMount.current === currentOrganizationId,
    ({ data }) =>
      Alert.alert(
        submitting ? "Request in progress" : "Discard this order?",
        submitting
          ? "Wait for the current request to finish."
          : "Your unsaved order will be lost.",
        submitting
          ? [{ text: "OK" }]
          : [
              { text: "Keep editing", style: "cancel" },
              {
                text: "Discard",
                style: "destructive",
                onPress: () => navigation.dispatch(data.action),
              },
            ],
      ),
  );
  const quoteKey = JSON.stringify(estimateKey(form.values));
  const previousQuoteKey = useRef(quoteKey);
  useEffect(() => {
    if (previousQuoteKey.current !== quoteKey) {
      setEstimates([]);
      void form.setFieldValue("estimateId", "", false);
      form.setStatus(undefined);
    }
    previousQuoteKey.current = quoteKey;
  }, [quoteKey, form.setFieldValue, form.setStatus]);
  return {
    form,
    step,
    estimates,
    selected: form.values.estimateId,
    error: form.status as string | undefined,
    submitting,
    created,
    setSelected: (id: string) => void form.setFieldValue("estimateId", id),
    back: () => {
      form.setStatus(undefined);
      setStep((value) => Math.max(0, value - 1));
    },
    next: () => {
      form.setStatus(undefined);
      if (submitting || created) return;
      if (step === 1 && form.isValid) setStep(2);
      else if (step === 0 || step === 2) void form.submitForm();
    },
    requestOptions: () => form.submitForm(),
    done: () => {
      if (!created) return;
      if (!access.orders) {
        navigation.goBack();
        return;
      }
      navigation.dispatch((state) => {
        const next = ordersSectionRoutes(state.routes, "delivery");
        next.push({
          key: `order-${created.id}`,
          name: routes.orderDeliveryDetails,
          params: { orderId: created.id },
        });
        return CommonActions.reset({
          ...state,
          routes: next,
          index: next.length - 1,
        });
      });
    },
  };
};

```

## Scoped reference verification

Codex inspected SERLP Mobile `src/crm/createCustomer/CreateCustomer.tsx`, its `useCreateCustomerForm.ts`, and `src/hrm/hrmSettings/hooks/useClockInSettingsForm.ts`. These show direct screen field bindings, ordinary Yup field rules including number/min/required, a named typed Formik hook, and one-time seeding of asynchronously fetched data. The live Altin source has been renamed by the user to `src/orders/createOrder`; do not restore the old directory. These are repository observations, not user approval of any replacement implementation.
