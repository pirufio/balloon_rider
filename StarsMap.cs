using Godot;
using System;
using System.Linq;

public partial class StarsMap : Node2D
{
	private Player player; 
	HudCanvasLayer hud;

	public HudCanvasLayer Hud => hud;

	private int numStars= 25;
	double elapsedTime = 0.0;
	PackedScene scene = GD.Load<PackedScene>("res://star_enemy.tscn");
	private Vector2 wSize;
	private bool isLow = false;
	double elapsedTimeLow = 0.0;
	private Fish fish;
	float fishY = 0;
	float fishX = 0;
	private bool isFishHunting = false;
	public override void _Ready()
	{
		wSize = DisplayServer.WindowGetSize();
		player = GetNode<Player>("Player");
		hud = (HudCanvasLayer)GetNode<Node2D>("Hud");
		fish = GetNode<Fish>("Fish");
		fish.Position = new Vector2(wSize.X / 2, wSize.Y + 36);
		fish.Visible = false;
	}
	
	void SpawnStar() {	
		StarEnemy instance = (StarEnemy)scene.Instantiate();
		AddChild(instance);
		var rng = new RandomNumberGenerator();
		float x = wSize.X - 16;
		float y = rng.RandfRange(0, wSize.Y);
		var transform = instance.Transform;
		transform.Origin = new Vector2(x, y);
		instance.Transform = transform;
	}

	public override void _PhysicsProcess(double delta)
	{
		fish.PlayerPosition(player.Position);

		bool drawn = false;
		if (wSize.Y > 0 && player.Position.Y > (wSize.Y + 40))
		{
			elapsedTimeLow = 0;
			drawn = true;
		}
		else if (wSize.Y > 0 && player.Position.Y > (wSize.Y - 120))
		{
			isLow = true;
			elapsedTimeLow+= delta;
		}
		else
		{
			elapsedTimeLow = 0;
			isLow = false;
		}


		elapsedTime += delta;
		var rng = new RandomNumberGenerator();
		float rand = rng.RandfRange(0.2f, 0.9f);
		if (elapsedTime >= (double)rand)
		{
			elapsedTime = 0;
			SpawnStar();
			hud.Points += 1;
		}

		var collision = player.MoveAndCollide(player.Velocity * (float)delta);
		if (collision != null || drawn)
		{
			hud.Lives -= 1;
			if (hud.Lives > 0)
			{
				ShowLoseLifeMessage($"Life Lost! {hud.Lives} remaining.");
			}
			if (hud.Lives <= 0)
			{
				ShowLoseLifeMessage("Game Over!");
			}
		}
	}

	public void GameOver()
	{
		GD.Print("GAME OVER");
		GetTree().ReloadCurrentScene();
		var scene = ResourceLoader.Load<PackedScene>("res://main_menu.tscn").Instantiate();
		GetTree().Root.AddChild(scene);
		GetTree().Root.RemoveChild(this);
	}

	public void ContinueGame()
	{
		GD.Print("CONTINUE GAME");
		foreach (var item in (this.GetChildren().Where(x => x is StarEnemy)))
		{
			{
				item.Free();
			}
			player.Position = new Vector2(250f, 320f);
		}
	}

	private void ShowLoseLifeMessage(string message)
	{
		// Pause the entire game tree
		GetTree().Paused = true;
		// Instantiate the message scene
		LoseLifeMessage loseLifeMessageInstance = (LoseLifeMessage)ResourceLoader.Load<PackedScene>("res://lose_life_message.tscn").Instantiate();
		loseLifeMessageInstance.ProcessMode = ProcessModeEnum.Always;
		GetTree().Root.AddChild(loseLifeMessageInstance); // Add to the root to be on top
		// Set the message text
		loseLifeMessageInstance.SetMessage(message, this);
		
	}

}
