<script>
    import { Form, Input } from '$lib/components/ui/form.svelte';

</script>

<div >

 <Form.Field {form} name="email">
    <Form.Control let:attrs>
      <Form.Label>Login Name</Form.Label>
      <Input {...attrs} bind:value={$formData.email} />
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>
  <Form.Field {form} name="password">
    <Form.Control let:attrs>
      <Form.Label>Password</Form.Label>
      <Input type="password" {...attrs} bind:value={$formData.password} />
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>

</div>


<!-- Compare this snippet from conti-platform/resources/lib/components/auth/RequestAccount/RequestAccountForm.svelte: -->