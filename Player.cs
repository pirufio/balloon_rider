using Godot;
using System;

public partial class Player : CharacterBody2D
{
	[Signal]
	public delegate void HitEventHandler();
	private AnimatedSprite2D _animatedSprite;
	
	private float jump_velocity = 1.2f;
	private float fall_speed = .4f;
	private float gravity = (float)ProjectSettings.GetSetting("physics/2d/default_gravity");
	[Export]
	public int Speed { get; set; } = 200;

	public override void _Ready()
	{
		_animatedSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		_animatedSprite.Play("idle");
	}
	
	 public void GetInput() {
		Vector2 inputDirection = Input.GetVector("left", "right", "up", "down");
		inputDirection.Y += fall_speed;
		
		if (Input.IsActionPressed("jump"))
		{
			inputDirection.Y -= jump_velocity;	
		}
		
		if (Input.IsActionPressed("left"))
		{
			_animatedSprite.FlipH = true;	
		} else if (Input.IsActionPressed("right")) {
			_animatedSprite.FlipH = false;
		}
			
		Velocity = inputDirection * Speed;
		
		if(Velocity.Y < 0){
			_animatedSprite.Play("fly");
		} else {
			_animatedSprite.Play("idle");
		}
	}
	
	public override void _PhysicsProcess(double delta)
	{
		GetInput();
		MoveAndSlide();
	}
}
