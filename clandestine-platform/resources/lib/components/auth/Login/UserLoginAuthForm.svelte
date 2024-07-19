<script>
    import { Form, Input } from '$lib/components/Form.svelte';
    import { createForm } from '$lib/forms';
    import { useLogin } from '$lib/api/auth';
    import AuthForm from '../Form/AuthForm.svelte';
    const form = createForm({
        email: {
            required: true,
            type: 'email',
        },
        password: {
            required: true,
        },
    });

    const $formData = form.data;

    async function submit() {
        if (!form.validate()) return;

        try {
            await useLogin($formData);
            form.reset();
            alert('Login successful');
        } catch (error) {
            alert('Failed to login');
        }
    }


</script>

<div class="flex flex-col space-y-2 text-center">
    <h1 class="text-2xl font-semibold tracking-tight">Login</h1>
    <p class="text-sm text-muted-foreground">
        Enter your credentials below to login to the platform.
    </p>
    <form method="POST" use:enhance>
        
        <button type="button" class="btn btn-primary" on:click={submit}>
            Login
        </button>
    </form>
</div>