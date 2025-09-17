using Godot;
using System;

public partial class Fish : CharacterBody2D
{
	private Vector2 _playerPosition;
	private Sprite2D _sprite;

	[Export]
	public float JumpHeight = 200.0f; // The peak height of the jump in pixels.
	[Export]
	public float JumpTimeToPeak = 0.5f; // Time it takes to reach the peak of the jump.
	[Export]
	public float HorizontalSpeed = 150.0f; // The horizontal speed of the fish during its jump.

	private Vector2 _startPosition;
	private Vector2 _targetPosition;
	private float _jumpVelocityY;
	private float _gravity;
	private bool _isAttacking = false;
	private Node2D _player;
	private readonly int _attackThreshold = 120;

	public override void _Ready()
	{
		_sprite = GetNode<Sprite2D>("Sprite2D");
		var image = Image.LoadFromFile("res://sprites/fish.png");
		var texture = ImageTexture.CreateFromImage(image);
		_sprite.Texture = texture;
		// Calculate gravity and initial jump velocity based on desired height and time.
		_gravity = 2 * JumpHeight / (JumpTimeToPeak * JumpTimeToPeak);
		_jumpVelocityY = -_gravity * JumpTimeToPeak;

		// Hide the fish initially.
		Visible = false;
	}
	public override void _PhysicsProcess(double delta)
	{
		GD.Print("Fish pos: ", Position.X, Position.Y, " player pos: ", _playerPosition.X, _playerPosition.Y);
		
		if ((Position.X - _playerPosition.X <= _attackThreshold) && (Position.Y - _playerPosition.Y <= _attackThreshold) && !_isAttacking)
		{
			TriggerAttack();
		} else if (!_isAttacking)
		{
			Position = new Vector2(_playerPosition.X, Position.Y);

		}

		if (_isAttacking)
		{
			// Apply gravity.
			Vector2 velocity = Velocity;
			velocity.Y += _gravity * (float)delta;

			// Move the fish.
			Velocity = velocity;
			MoveAndSlide();

			// Check if the fish is off-screen at the bottom again.
			if (GlobalPosition.Y > GetViewportRect().Size.Y + 50)
			{
				// Reset for the next attack.
				_isAttacking = false;
				GD.Print("Fish is not Attacking");
				Visible = false;
				//SetPhysicsProcess(false);
				//GlobalPosition = _startPosition;
			}
		}
	}

	private void TriggerAttack()
	{
		GD.Print("Trigger Attack");
		// Make the fish visible and enable its physics processing.
		Visible = true;

		_isAttacking = true;
		_startPosition = GlobalPosition;
		_targetPosition = _playerPosition;

		// Calculate the direction towards the player.
		Vector2 direction = (_targetPosition - _startPosition).Normalized();

		// Set the initial velocity for the jump.
		Velocity = new Vector2(direction.X * HorizontalSpeed, _jumpVelocityY);
	}

	public void PlayerPosition(Vector2 playerPosition)
	{
		_playerPosition = playerPosition;
	}
}
