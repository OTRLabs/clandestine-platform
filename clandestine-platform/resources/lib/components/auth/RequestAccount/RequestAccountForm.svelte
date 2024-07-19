<script>
    import { Form, Input, Textarea } from '$lib/components/Form.svelte';
    import { createForm } from '$lib/forms';
    import { useRequestAccount } from '$lib/api/auth';

    const form = createForm({
        email: {
            required: true,
            type: 'email',
        },
        message: {
            required: true,
        },
    });

    const $formData = form.data;

    async function submit() {
        if (!form.validate()) return;

        try {
            await useRequestAccount($formData);
            form.reset();
            alert('Request sent successfully');
        } catch (error) {
            alert('Failed to send request');
        }
    }


</script>

<div class="flex flex-col space-y-2 text-center">
    <h1 class="text-2xl font-semibold tracking-tight">Want an account?</h1>
    <p class="text-sm text-muted-foreground">
        Enter your request in the form below to contact the platform admins.
    </p>
    <form method="POST" use:enhance>
        <Form.Field {form} name="email">
          <Form.Control let:attrs>
            <Form.Label>Email</Form.Label>
            <Input {...attrs} bind:value={$formData.email} />
          </Form.Control>
          <Form.Description />
          <Form.FieldErrors />
        </Form.Field>
        <Form.Field {form} name="message">
          <Form.Control let:attrs>
            <Form.Label>Message</Form.Label>
            <Textarea {...attrs} bind:value={$formData.message} />
          </Form.Control>
          <Form.Description />
          <Form.FieldErrors />
    </form>
</div>