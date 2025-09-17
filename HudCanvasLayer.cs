using Godot;
using System;

public partial class HudCanvasLayer : Node2D
{
	private Label labelPoints;
	private Label labelLives;
	[Export]
	public int Points { get; set; } = 1;
	[Export]
	public int Lives { get; set; } = 3;
	

	public override void _Ready()
	{
		labelPoints = GetNode<CanvasLayer>("CanvasLayer").GetNode<Label>("LabelPoints");
		labelLives = GetNode<CanvasLayer>("CanvasLayer").GetNode<Label>("LabelLives");
	}
	

	public override void _PhysicsProcess(double delta)
	{
		labelPoints.Text = "Points: " + Points;
		labelLives.Text = "Lives: " + Lives;
	}
	
	
}
