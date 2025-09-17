using Godot;
using System;

public partial class StarEnemy : CharacterBody2D
{
	[Export]
	public int Speed { get; set; } = 75;
	private AnimatedSprite2D _animatedSprite;
	
	public override void _Ready()
	{
		_animatedSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
		_animatedSprite.Play("default");
	}
	
	public override void _PhysicsProcess(double delta)
	{
		Vector2 direction = new Vector2(-1, 0);
		Velocity = direction * Speed;
		MoveAndSlide();
	}
	
	
}
